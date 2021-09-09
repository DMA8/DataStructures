# Очереди с приоритетом
# Абстрактный тип данных
# Поддерживает след операции

# Classic algorithms
# Алгоритм Дейкстры - ищет минимальный путь в графе
# Агроритм Прима - построение минимального покрывающего дерева
# Алгоритм Хаффмана - строит оптимальное безпрефиксное кодирование
# Алгорит сортировки кучей

# ДВОИЧНАЯ КУЧА
# двоичная макс куча - двоичнео дерево (у каждой вершины не более двух сыновей)
# в котором значение в каждой вершине не меньше чем значения в ее сыновьях

def insert(priority, heap): # ПОВЕСИТЬ К ЛИСТУ И ПРОСЕИТЬ ВВЕРХ
    # ЧИНИМ КУЧУ
    """inserting new elem with 'priority'"""
    heap.append(priority)
    siftup(len(heap) - 1, heap)
def extractmax(heap): # ИЗВЛЕКАЕМ КОРЕНЬ, НА ЕГО МЕСТО КИДАЕМ ЛИСТ
    # ПРОВЕРЯЕМ СВОЙСТВО КУЧИ - ПРОСЕИВАЕМ ВНИЗ. МЕНЯЕМ С НАИБОЛЬШИМ ИЗ ДЕТЕЙ
    #
    """extract elem with max priority"""
    result = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    siftdown(0, heap)
    return result
def remove(elem, heap): # ДАЕМ ЭЛЕМЕНТУ БЕСКОНЕЧНЫЙ ПРИОРИТЕТ И ДЕЛАЕМ ЭКСТРАКТ МАКС
    # changepriority() + extractmax()
    """remove given elem from heap"""
    heap[elem] = 10**10
    siftup(elem, heap)
    extractmax(heap)
def getmax(heap):
    """return elem with max priority"""
    return heap[0]
def changepriority(elem, priority, heap):
    """change prior of given elem to 'priority' """
    old = heap[elem]
    heap[elem] = priority
    if priority > old:
        siftup(elem, heap)
    else:
        siftdown(elem, heap)
def lchild(ind, heap):
    if 2 * ind + 1 < len(heap):
        return 2 * ind + 1
def rchild(ind, heap):
    if 2 * ind + 2 < len(heap):
        return 2 * ind + 2
def parent(ind, heap):
    return int((ind - 1) / 2)
def siftup(ind, heap):
    while ind > 0 and heap[parent(ind, heap)] < heap[ind]:
        heap[parent(ind, heap)], heap[ind] = heap[ind], heap[parent(ind, heap)]
        ind = parent(ind, heap)
ans = []
def minsiftup(ind, heap):
    while ind < len(heap) and heap[parent(ind, heap)] > heap[ind]:
        ans.append([heap[parent(ind, heap)], heap[ind]])
        heap[parent(ind, heap)], heap[ind] = heap[ind], heap[parent(ind, heap)]
        ind = parent(ind, heap)

def siftdown(ind, heap, len_heap=0):
    maxindex = ind
    if not len_heap: len_heap = len(heap)
    left = lchild(ind, heap)
    if left and ind < len_heap and heap[left] > heap[maxindex]:
        maxindex = left
    right = rchild(ind, heap)
    if right and right < len_heap and heap[right] > heap[maxindex]:
        maxindex = right
    if ind != maxindex:
        heap[ind], heap[maxindex] = heap[maxindex], heap[ind]
        siftdown(maxindex, heap)

def minsiftdown(ind, heap, len_heap=0):
    minindex = ind
    if not len_heap: len_heap = len(heap)
    left = lchild(ind, heap)
    if left and ind < len_heap and heap[left] < heap[minindex]:
        minindex = left
    right = rchild(ind, heap)
    if right and right < len_heap and heap[right] < heap[minindex]:
        minindex = right
    #    print("here")
    if ind != minindex:
        ans.append([ind, minindex])
        heap[ind], heap[minindex] = heap[minindex], heap[ind]
        minsiftdown(minindex, heap)

def maxbuildheap(heap:list):
    for i in range(int(len(heap) / 2), -1, -1):
        siftdown(i, heap)
def minbuildheapup(heap:list):
    for i in range(0, len(heap)):
        minsiftup(i, heap)

def minbuildheapdown(heap:list):
    for i in range(int(len(heap) / 2 + 1), -1, -1):
        minsiftdown(i, heap)

def check_max_heap(heap:list):
    for i in range(1, len(heap)):
        if heap[i] < heap[parent(i, heap)]:
            continue
        else:
            print("IT'S NOT A MAXHEAP")
            return
    print("IT'S A MAX HEAP!")
def check_min_heap(heap:list):
    for i in range(1, len(heap)):
        if heap[i] > heap[parent(i, heap)]:

            continue
        else:
            print("IT'S NOT A MINHEAP")
            return
    print("IT'S A MIN HEAP!")

if __name__ == '__main__':
    
    input()
    hp = input().split()
    for i in range(len(hp)):
        hp[i] = int(hp[i])
    minbuildheapdown(hp)
    print(len(ans))
    for i in ans:
        for j in i:
            print(j, end=' ')
        print()

# НУЖНО ДЕРЖАТЬ ДЕРЕВО МАКСИМАЛЬНО НЕВЫСОКИМ
# ЕСЛИ ДЕРЕВО ЗАПОЛНЕНО ПОЛНОСТЬЮ, ТО ЕГО ВЫСОТА log(N) - число элементов в дереве
# Дерево удобно хранить в массиве, где индекс элемента - позиция элемента. А значение в массиве - приоритет

# Индекс родителя = index / 2
# Left child = 2 * index
# Right child = 2 * index + 1

# КАК ПОДДЕРЖИВАТЬ ДЕРЕВО ПОЛНОСТЬЮ ЗАПОЛНЕННЫМ?
# Только inset и extractmax изменяют форму дерева
# Инсертим в первое вакантное место
# extractmax - удаляем макс число, потом меняем последний элемент кучи с корнем и просеиваем вниз
