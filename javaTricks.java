// print a map
private final ConcurrentMap<String, AtomicLong> throttledRequestsByUser = getVarzMap(varzMapName);
System.out.println(Arrays.toString(throttledRequestsByUser.entrySet().toArray()));
