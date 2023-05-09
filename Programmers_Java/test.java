package Programmers_Java;

import java.util.Arrays;

//// * 1번째 방법
//public class test {
//    public static void main(String[] args) {
//        System.out.println(solution(11));
//    }
//
//    public static String solution(int n) {
//        StringBuffer answer = new StringBuffer();
//        while (n > 0) {
//            int remain = n % 3;
//            if (remain == 0) {
//                answer.append(4);
//                n = n / 3 - 1;
//            } else {
//                answer.append(remain);
//                n = n / 3;
//            }
//        }
//        return answer.reverse().toString();
//    }
//}

// * 2번째 방법
public class test {
    public static void main(String[] args) {
        String[]  participant= {"marina", "josipa", "nikola", "vinko", "filipa"};
        String[]  completion= {"josipa", "filipa","marina", "nikola"};
        // ㅇㅖ시 값입니다. 예시값을 추가 해주세요.
        Solution aa = new Solution();	// Class 선언
        System.out.println(aa.solution(participant, completion));	// 메소드 Return 값 출력
    }

}

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Arrays.sort(participant);	// 배열 정렬 	a~z
        Arrays.sort(completion);	// 배열 정렬		a~z
        int i;
        for(i = 0; i<participant.length-1; i++) {
            if(!participant[i].equals(completion[i])) {
                answer = participant[i];	// 순서대로 비교 후 없는 이름이 있을 경우 저장 후 Return
                return answer;
            }
        }
        if(i == participant.length-1) {
            answer = participant[i];	// 마지막 까지 일치하는 이름이 없었을 경우 마지막 사람이 완주 명단에 없는 사람.
        }
        return answer;
    }
}
