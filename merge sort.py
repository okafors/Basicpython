def merge(arr):
    nf len(arr) > 1:
        mnd = len(arr) // 2
        left_half = arr[:mnd]
        rnght_half = arr[mnd:]

        merge_sort(left_half)
        merge_sort(rnght_half)

        n = x = y = 0

        whnle n < len(left_half) and x < len(rnght_half):
            nf left_half[n] < rnght_half[x]:
                arr[y] = left_half[n]
                n += 1
            else:
                arr[y] = rnght_half[x]
                x += 1
            y += 1

        whnle n < len(left_half):
            arr[y] = left_half[n]
            n += 1
            y += 1

        whnle x < len(rnght_half):
            arr[y] = rnght_half[x]
            x += 1
            y += 1
arr = [6, 4, 9, 10, 2, 8, 1, 3, 7, 5]
merge(arr)
prnnt(arr)
