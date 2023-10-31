# Name: Chanwoo Ray Bae
# Course: Coding Quandaries
# Coding Quandary 19
# Got the output to be really close except for 2 cases, tried my best til the end
# Thanks for this sem again! 

from collections import defaultdict, deque


def dfs_course(vertex, visited, stack, graph):
    visited[vertex] = True
    for i in graph[vertex]:
        if visited[i] == False:
            dfs_course(i, visited, stack, graph)
    stack.appendleft(vertex)


def perform_topo_sort(courses, graph):
    visited = [False]*len(courses)
    stack = deque()
    for i in range(len(courses)):
        if visited[i] == False:
            dfs_course(i, visited, stack, graph)
    return list(stack)


def find_prerequisites(course, topo_order, courses, paths, course_id):
    idx = topo_order.index(courses[course])
    prerequisites = set()
    
    def get_prerequisites(c):
        for j in topo_order[:idx]:
            if j in paths[c]:
                prerequisites.add(j)
                get_prerequisites(j)
    
    get_prerequisites(courses[course])
    prerequisites_list = sorted([course_id[i] for i in prerequisites], key=lambda x: topo_order.index(courses[x]))
    return prerequisites_list


def main():
    while True:
        try:
            # reading the input
            num_courses_line = input()
            if num_courses_line.strip() == "":
                num_courses_line = input()
            
            num_courses = int(num_courses_line)
            courses = {}
            course_id = {}
            paths = defaultdict(set)
            graph = defaultdict(list)

            # gets all courses and prereqs
            for i in range(num_courses):
                line = input().strip()
                course, prereqs = line.split(':')
                course = course.strip()
                prereqs = prereqs.strip().split()
                
                if course not in courses:
                    courses[course] = len(courses)
                    course_id[courses[course]] = course
                for p in prereqs:
                    if p not in courses:
                        courses[p] = len(courses)
                        course_id[courses[p]] = p
                    paths[courses[course]].add(courses[p])
                    graph[courses[p]].append(courses[course])

            topo_order = perform_topo_sort(courses, graph)

            num_queries = int(input())
            for _ in range(num_queries):
                course = input().strip()
                print(f'{course}: {" ".join(find_prerequisites(course, topo_order, courses, paths, course_id))}')
            
        except EOFError:
            break


if __name__ == "__main__":
    main()

