import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Random;

public class Sort {
    public static void main(String[] args) {
        Random random = new Random();
        Sort sort = new Sort();

        int n = (int)Math.pow(2, 20);
        int[] array = new int[n];
//        Integer[] array = new Integer[n];
        for (int j=0; j < n; j++){
            array[j] = random.nextInt(n);
        }
//        Arrays.sort(array, Collections.reverseOrder()); // 배열을 역순으로 정렬
        Arrays.sort(array);

        System.out.println("정렬된 배열 생성 완료, 시간 측정 시작");
        long start = System.nanoTime();
        sort.ShellSort(array);
        long end = System.nanoTime();
        System.out.println("소요 시간 : " + (end - start)+ " ns");

//        for (int i=0; i<array.length; i++){
//            System.out.printf(array[i] + " ");
//        }
    }
    public void BubbleSort(int[] array){
        for (int i=0; i<array.length; i++){
            for (int j=0; j<array.length-i-1; j++){
                if (array[j] > array[j+1]){
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    }
    public void SelectionSort(int[] array){
        for (int i=0; i<array.length; i++){
            int min = array[i];
            int index = i;
            for (int j=i+1; j<array.length; j++){
                if (min > array[j]){
                    min = array[j];
                    index = j;
                }
            }
            int temp = array[i];
            array[i] = array[index];
            array[index] = temp;
        }
    }
    public void InsertionSort(int[] array){
        for (int i=1; i<array.length; i++){
            int current_element = array[i];
            int j = i - 1;
            while (j >= 0 && array[j] > current_element){
                array[j+1] = array[j];
                j -= 1;
            }
            array[j+1] = current_element;
        }
    }
    public void ShellSort(int[] array){
        int[] gap = {5,4,3,2,1};
        for (int h : gap) {
            for (int i=h; i<array.length; i++){
                int current_element = array[i];
                int j = i;
                while (j >= h && array[j-h] > current_element){
                    array[j] = array[j-h];
                    j -= h;
                }
            array[j] = current_element;
            }
        }
    }
    public void HeapSort(int[] array){
        PriorityQueue priorityQueue = new PriorityQueue();
        int index = 0;
        for(int i : array) {
            priorityQueue.add(i);
        }
        while(!priorityQueue.isEmpty()){
            array[index] = (int)priorityQueue.remove();
            index++;
        }
    }
    public void QuickSort(int[] array){
        Arrays.sort(array);
    }
}
