# switch between java versions
# usage: use-java 7

use-java () {
    export JAVA_HOME=`/usr/libexec/java_home -v 1.$1`
}
