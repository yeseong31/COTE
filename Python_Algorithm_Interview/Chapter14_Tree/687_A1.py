# 풀이 1 - 상태값 거리 계산 DFS


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            # 존재하지 않는 노드까지 dfs 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 백트래킹 수행
            # 현재 노드가 자식 노드와 동일한 경우에 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 최종 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴 (상태값을 세팅해서 부모 노드로 올림)
            return max(left, right)

        dfs(root)
        return self.result
