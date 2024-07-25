def merge(A, start, mid, end, buff):
        left = start
        right = mid + 1
        s = end - start + 1

        for i in range(s):
            i0 = start + i
            if left > mid:
                buff[i0] = A[right]
                right += 1
            elif right > end:
                buff[i0] = A[left]
                left += 1
            elif A[left] < A[right]:
                buff[i0] = A[left]
                left += 1
            else:
                buff[i0] = A[right]
                right += 1

        for i in range(start, start + s):
            A[i] = buff[i]

    def merge_sort(A, start, end, buff):
        if end <= start:
            return
        mid = start + (end - start) // 2
        merge_sort(A, start, mid, buff)
        merge_sort(A, mid + 1, end, buff)
        merge(A, start, mid, end, buff)
