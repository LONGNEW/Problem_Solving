import java.io.*;
import java.util.*;

public class Main {
    public static class Node implements Comparable<Node>{
        int start;
        int end;

        Node(int start, int end){
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Node o) {
            if(o.end != this.end)
                return this.end - o.end;

            return this.start - o.start;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        Node[] list = new Node[N];

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            list[i] = new Node(s, e);
        }

        Arrays.sort(list);
        TreeMap<Integer, Integer> map = new TreeMap<>();

        if(K != 1)
            map.put(0, K - 1);

        int count = 0, time = 0;
        for(int i = 0; i < N; i++) {
            Node curNode = list[i];
            int curStart = curNode.start;
            int curEnd = curNode.end;

            if(time >= curStart)
                continue;

            if(map.lowerKey(curStart) == null) {
                count++;
                time = curEnd;
            }
            else {
                int tmp = map.lowerKey(curStart);

                if(map.get(tmp) == 1)
                    map.remove(tmp);
                else
                    map.put(tmp, map.get(tmp) - 1);

                if(map.containsKey(curEnd))
                    map.put(curEnd, map.get(curEnd) + 1);
                else
                    map.put(curEnd, 1);
            }
        }

        System.out.println(count);
    }
}