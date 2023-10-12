"""
# 간단한 다익스트라 알고리즘
* 단계마다 ‘방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택’하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)
"""
import sys

# input = sys.stdin.readline() # input : 입력한 문자열
input = sys.stdin.readline  # 객체
# print(input)

INF = int(1e9)  # 무한의미 10억

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드 정보 담는 리스트
graph = [[] for i in range(n + 1)]
