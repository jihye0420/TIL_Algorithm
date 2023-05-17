# https://lovelyalien.tistory.com/116
package Programmers_Python.TEST;

public class test18 {
}


public class Solution {

    static Set<Integer> answerSet = new HashSet<>();
    static int sum = 0;

    public int solution(int k, int[] numbers) {


        permutation(numbers, 0, 0, k, numbers.length);

        int answer = answerSet.stream().min(Integer::compare).orElse(-1);
        System.out.println(sum);
        return answer;


    }

    static void permutation(int[] numbers, int depth, int cnt, int k, int N) {
        if (depth == N) {
            sum += 1;
            boolean flag = true;
            for (int i = 1; i < numbers.length; i++) {
                if (Math.abs(numbers[i - 1] - numbers[i]) > k) {
                    flag = false;
                    break;
                }

            }
            if (flag)
                answerSet.add(cnt);

            System.out.println(Arrays.toString(numbers));
        }

        for (int i = depth; i < N; i++) {

            swap(numbers, depth, i);
            //swap 발생
            if (depth != i)
                permutation(numbers, depth + 1, cnt + 1, k, N);
                //depth==i
                //swap 발생 X
            else
                permutation(numbers, depth + 1, cnt, k, N);

            swap(numbers, depth, i);
        }
    }

    static void swap(int[] numbers, int depth, int i) {
        int tmp = numbers[depth];
        numbers[depth] = numbers[i];
        numbers[i] = tmp;
    }
}