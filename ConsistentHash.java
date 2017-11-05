import java.util.Arrays;
import java.util.List;
import java.util.Collection;  
import java.util.SortedMap;  
import java.util.TreeMap;  
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.io.UnsupportedEncodingException;
import java.nio.ByteBuffer;


public class ConsistentHash<T> {  

  private final MessageDigest hashFunction;
  private final int numberOfReplicas;  
  private final SortedMap<Integer, T> circle = new TreeMap<Integer, T>();  

  public ConsistentHash(int numberOfReplicas,
                        Collection<T> nodes)
                        throws NoSuchAlgorithmException,
                               UnsupportedEncodingException {
    this.hashFunction = MessageDigest.getInstance("MD5");
    this.numberOfReplicas = numberOfReplicas;  
    for (T node : nodes) {  
      add(node);  
    }  
  }  

  private Integer hash(String str) throws UnsupportedEncodingException {
    byte[] bytesOfMessage = str.getBytes("UTF-8");
    byte[] theDigest = hashFunction.digest(bytesOfMessage);
    ByteBuffer wrapped = ByteBuffer.wrap(theDigest);
    return wrapped.getInt();
  }

  public void add(T node) throws UnsupportedEncodingException {
    for (int i = 0; i < numberOfReplicas; i++) {  
      circle.put(hash(node.toString() + i), node);  
    }  
  }  

  public void remove(T node) throws UnsupportedEncodingException {
    for (int i = 0; i < numberOfReplicas; i++) {  
      circle.remove(hash(node.toString() + i));  
    }  
  }  

  public T get(Object key) throws UnsupportedEncodingException {
    if (circle.isEmpty()) {  
      return null;  
    }  
    int hash = hash(key.toString());  
    if (!circle.containsKey(hash)) {  
      SortedMap<Integer, T> tailMap = circle.tailMap(hash);  
      hash = tailMap.isEmpty() ?  
             circle.firstKey() : tailMap.firstKey();  
    }  
    return circle.get(hash);  
  }   

  public static void main(String[] args) {
    System.out.println("sup");
    // TODO: call w/the right method signature.
    List<String> nodes = Arrays.asList("a", "b", "c");
    ConsistentHash ch = ConsistentHash(5, nodes);
  }
}

