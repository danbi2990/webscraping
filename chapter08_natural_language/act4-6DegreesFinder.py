from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='dnwls895', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE wikipedia")


class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message


def getLinks(fromPageId):
    cur.execute("SELECT toPageId from links where fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]


def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links)))
    return {}


# 링크 트리가 비어 있거나 링크가 여러 개 들어 있습니다.
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        # 재귀를 중지하고 함수를 끝냅니다.
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            # 링크가 발견되지 않았으므로 이 노드에서는 계속할 수 없습니다.
            return {}
    if targetPageId in linkTree.keys():
        print("Target "+str(targetPageId)+" FOUND!")
        raise SolutionFound("PAGE: "+str(currentPageId))

    for branchKey, branchValue in linkTree.items():
        try:
            # 재귀적으로 돌아와서 링크 트리를 구축합니다.
            linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("PAGE: "+str(currentPageId))
    return linkTree


try:
    # searchDepth(134951, 1, {}, 4)
    searchDepth(15622, 1, {}, 4)
    print("No solution found")
except SolutionFound as e:
    print(e.message)
finally:
    cur.close()
    conn.close()
