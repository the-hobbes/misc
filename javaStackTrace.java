/**
  Use this snippet to get a stacktrace of calls at a point in your application.
  http://stackoverflow.com/questions/421280/how-do-i-find-the-caller-of-a-method-using-stacktrace-or-reflection.
*/

    StackTraceElement[] stackTraceElements = Thread.currentThread().getStackTrace();
    for (StackTraceElement item : stackTraceElements) {
        System.out.println(item.getMethodName());
        //getClassName() is also supported, along with several others
    }
