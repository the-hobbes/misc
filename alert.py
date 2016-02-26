"""Create a tweakable model to plan alert parameters."""


class Alert():
    """Represents an alert."""
    def __init__(self,
                 alert_type,
                 slo_ratio,
                 slo_period,
                 slo_exhaustion_duration,
                 slo_fraction_per_alert):
        self.alert_type = alert_type
        self.slo_ratio = slo_ratio
        self.slo_period = slo_period
        self.slo_exhaustion_duration = slo_exhaustion_duration
        self.slo_fraction_per_alert = slo_fraction_per_alert

        self.alert_threshold = (1 - self.slo_ratio) * (self.slo_period / self.slo_exhaustion_duration)
        self.alert_window = self.slo_exhaustion_duration * self.slo_fraction_per_alert
        self.outage_response = self.alert_threshold * self.alert_window

    def PrintAlert(self):
        """Prints information about the alert."""
        print '*** %s ***' % self.alert_type
        print 'alert_threshold: %s' % self.alert_threshold
        print 'alert_window (in minutes): %s, (in hours): %s' % (self.alert_window, self.alert_window / 60)
        print 'outage_response (in minutes): %s \n' % self.outage_response

    def OutageResponse(self):
        print '*** %s outage response ***' % self.alert_type
        print '100 percent: %s minutes' % (1 * self.outage_response)
        print '10 percent: %s minutes' % ((1/.1) * self.outage_response)
        print '1 percent: %s hours' % ((1/.01) * self.outage_response / 60)
        print '.1 percent: %s hours' % ((1/.001) * self.outage_response / 60)
        print 'Alert threshold: %s hours\n' % ((1 / self.alert_threshold) * self.outage_response / 60)


def test():
    """Test objects with known good values."""
    ticket_alert = Alert(alert_type='Ticketing',
                         slo_ratio=0.999,  # SLA
                         slo_period=40320.0,  # 28 days
                         slo_exhaustion_duration=14400.0,  # 10 days
                         slo_fraction_per_alert=.25)  # quarter of the 28 day error budget
    page_alert = Alert(alert_type='Paging',
                       slo_ratio=0.999,  # SLA
                       slo_period=43200.0,  # 28 days
                       slo_exhaustion_duration=5760.0,  # 4 days
                       slo_fraction_per_alert=1.0/16.0)  # 16th of the 28 day error budget
    ticket_alert.PrintAlert()
    page_alert.PrintAlert()


def main():
    ticket_alert = Alert(alert_type='Ticketing',
                         slo_ratio=0.9998,  # SLA
                         slo_period=43200.0,  # 30 days
                         slo_exhaustion_duration=18720.0,  # 13 days
                         slo_fraction_per_alert=.25)  # quarter of the 30 day error budget
    page_alert = Alert(alert_type='Paging',
                       slo_ratio=0.9998,  # SLA
                       slo_period=43200.0,  # 30 days
                       slo_exhaustion_duration=5750.0,  # 4 days
                       slo_fraction_per_alert=.2)  # a twentieth of the 30 day error budget
    ticket_alert.PrintAlert()
    ticket_alert.OutageResponse()
    page_alert.PrintAlert()
    page_alert.OutageResponse()

    # fastest slow burn
    fastest_slow_burn = (1.0 / page_alert.alert_threshold) * ticket_alert.outage_response
    print '\nfastest slow burn ratio (under paging threshold): %s' % page_alert.alert_threshold
    print 'this will consume the %s day error budget in %s day(s).' % ((page_alert.slo_period / 24 / 60), (page_alert.slo_exhaustion_duration / 24 / 60))
    print ('at this rate, after %s hours the ticket will fire.'
           ' This will give us %s days to respond before the whole budget is gone.'
           % (fastest_slow_burn / 60, (page_alert.slo_exhaustion_duration - fastest_slow_burn) / 60 / 24))


if __name__ == '__main__':
    main()
