# [트리]

# "순환 구조를 갖지 않는 그래프"
# 그래프와 달리, 트리는 부모 노드에서 자식 노드를 가리키는 단방향만 존재하며, 단 하나의 부모 노드와 루트 노드를 가진다.

# 트리 중에서도 가장 널리 사용되는 트리 자료구조는 이진 트리와 이진 탐색 트리이다.
# 먼저, 각 노드가 m개 이하의 자식을 갖고 있으면, m-ary 트리(다항 트리, 다진 트리)라고 한다.
# 여기서 m=2일 경우, 즉 모든 노드의 차수가 2 이하일 때는 특별히 이진 트리라고 구분해서 부른다.
# 대체로 트리라고 하면 특별한 경우가 아니고서는 대부분 이진 트리를 일컫는다.

# ------------------------------------------------------------------------------------------------------
# [이진 트리의 유형]
# (1) 정 이진 트리(Full Binary Tree)
#       - 모든 노드가 0개 또는 2개의 자식 노드를 가짐
#
# (2) 완전 이진 트리(Complete Binary Tree)
#       - 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있으며, 마지막 레벨의 모든 노드는 가장 왼쪽부터 채워져 있다.
#
# (3) 포화 이진 트리(Perfect Binary Tree)
#       - 모든 노드가 2개의 자식 노드를 갖고 있으며, 모든 리프 노드가 동일한 깊이 또는 레벨을 갖는다.
#       - 문자 그대로, 가장 완벽한 유형의 트리이다.

# ------------------------------------------------------------------------------------------------------
