---
title: 感觉写得很不错的一篇3100Report
date: 2019-10-15 15:01:04
abbrlink: 23181
---
# CSC3100 Assignment 1 Report
<h5> 姓名: `Sobadatsu Omo` </h5>
<h5> Student ID: `7182`</h5>

## **Decomposition of This Problem**
The problem is of a composite type. Through a simple decomposition method, we can divide this question into three smaller sections of more generic types. Firstly we need to **read streams of a static scale** through web servers. Secondly we need to **find out the exact positions** of two values of this stream of data. Thirdly we need to **varify a prime number** that was obtained by the subtraction of these two values.
## **Solutions for Each Section**
### **Read Streams of a Static Scale**
To read streams of a static scale through web servers, which can be recognized as a common instance of I/O data transmission. To solve it, we can use Scanner datatype, which is a widely applied file handler and can deal with a wide range of data sorts. I used to stick on it, until a cutting-edged technique "BufferedReader" has been revealed by my two of my friends, Xieguochao and Linyukun. 

The idea is that because the whole set of data streams is of the same datatype, so we do not need to worry about being interrupted by some strange data of different types that we do not have certain built-in methods to deal with. On the contract, as for "BufferedReader", the lack of generic functions can be regarded as a good save without a dummy type examinations in this case.

What's more, they have the same size which indicate that it can benefit memory alignment and block alignment. So it can be naturally designed to support buffers when dealing with a large scale of IO operations within high-speed devices and low-speed devices.
> `https://web.archive.org/web/20210512031900/https://stackoverflow.com/questions/2067096/is-the-memory-alignment-different-for-different-data-types`#2067244

So we use "BufferedReader" to deal with IO operations.
### **Find Out the Exact Positions of Two Values**
#### **Fully Sort is Costly**
The intuition of me is to sort the whole sequence. However, when we notice that the whole set has a large scale of numbers (up to 10000), while all we need is to determine two exact positions for two certain values, we can find that our intuition is somehow costly. 

But this can also serve as a booster of some inspiring ideas. For example, if I enlarge the objective values scale and reduce the dummy values scale, with the concentration of useful values increasing, of what extent will the original full sorting method "have some profits over other magic methods"? I will dive into some depth on it at future exploration part.
#### **Bucket Sort Can be Ruined by Sparse Sequence or Big h Value**
Now we focus on methods with no fully sorting operations. Some intuitions dawn on me that there can be some monitors inside, for example a counter, to watch and check whether a situation is a symbol of finishing all work and beginning to purely work on trash. If so, then we can call an end to this function and save some effort. 

So I come up with the "Partly" bucket sort method simultaneously. We create buckets on the way we visit the whole sequence, with a counter of elements number counting all elements that is smaller or bigger than the current one. If we manage it within two counters, then the cost will be very small!

However, as I test my program, I find that it can only perform well in the case when h value is small and the values have a dense distribution. It goes almost annoying when dealing with sparse sequence, and it has no privilege against original sorting methods when h value is big.
#### **Quick Sort Privilege on Partition and Scale Decreasing**

Quick sort is not my original intension where I will have a try, the key factor that quick sort can fantastically tackle this problem is the partition operation which quick sort relies on. Partition is a good way for those cases that need to maintain "some extent of order" without paying most more effort. The order of it is relevant to some typical values, like binary trees. 

In this cases, because the objective values are only two, so at the beginning of the procedure it may seem like a normal random function which pick all things without any partiality.  But as it cut off a good half of sequence every time it is placed, the speed to locate the objective value within a short interval will be tremendous, which can approach an exponential function with base 2.(Imagine!)

### **Varify a Prime Number**
#### Primitives: Prime Number Distributions
Mathematic nerds are born to be enthusiastic on magic numbers. I myself am nothing of them, but I am taught to know that prime numbers have a mysterious distribution on natural domains. A great Mathematic scholar, Riemann, established his Riemann Hypothesis that "very likely the distribution of prime numbers will be related with non-trivial zeros of Riemann zeta function".
> *`https://web.archive.org/web/20220606035649/https://www.cantorsparadise.com/the-riemann-hypothesis-explained-fa01c1f75d3f`*

I am nothing of a math guy, but it dawned on me that this theorem might be very useful when scientists are going to seek prime numbers among huge prime numbers. It can reduce a lot of dummy calculations on non-suspicious numbers.

The reason I say that much is to give you a context of prime numbers and it will be better for me to deliver my whole cargo. We can note from previous paragraphs and some related material that since prime numbers are getting 
more and more sparse when its amount goes immense, and as it has a distribution of this shape, we can apply a powerful method "sieve of Eratosthenes" to it.
> *`https://web.archive.org/web/20220531055104/https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes`*

(Please be careful with the prime numbers distribution! I know it is an intuition for people to think that "Because some small prime numbers can be the factor of big numbers, which can play a role as the big '
traitor' when a big number is going on its canonization prime-wise." Like this guy on quora. This is a very ambiguous mistake for scholars! I know you all have been highly educated and had much more insights than me, but this was truly a illusion for all of us. This is NOT the REASON for the prime numbers getting scarce! We can use this as a method for further estimation and analysis, but it is not THE REASON!)

#### **Application: Sieve of Eratosthenes**
> *The multiples of a given prime are generated as a sequence of numbers starting from that prime, with constant difference between them that is equal to that prime.[1] This is the sieve's key distinction from using trial division to sequentially test each candidate number for divisibility by each prime.*

I think it is none other than all the essence inside this filter. I will not waste any breathe on further elaborations. This is only one of those trivial jugglery that mathematics shows her patronization to poor men.

## **Further Explorations**
### **What if the Data Scale is not Static?**
This thought comes from a feature of BufferedReader, which shown below:
> *"BufferedReader is synchronous while Scanner is not. BufferedReader should be used if we are working with multiple threads."*

> *`https://web.archive.org/web/20160430035302/https://www.geeksforgeeks.org/difference-between-scanner-and-bufferreader-class-in-java/`*

As I know that BufferReader is synchronous and can be used to cope with multiple threads business, I doubt that whether it can be used to perform online processing. This is a much more complicated case since the dataset is engulfing in all the time. Can it do this job? if yes, how can / do BufferReader deal with their competitions?


### **Of What Extent will Full Sorting Method "have some profits over other magic methods"?**

I view this question on a strange perspective. Full sorting method can be regarded as every number takes up its own occupation correctly. But partly sorting method can be regarded as make some members take their correct places, and make some members take the wrong places.
As we can know that other values individually make no difference on objective numbers on partly sorting, but some groups may make some difference, for instance, if I want to find 4th largest number, then we have to manage that finally three numbers standing previously to the 4th largest number, but these three member can also switch their relevant positions, so it will generate 6 cases, that is to say, if a method of any kind, cannot deal with any n people's permulations standing behind an object within ∑n! steps, and then every sorting method can beat it. I now can only have limited ideas on this topic. I might further continue on it by consulting people or myself.

## **My Codes**
```java
import java.util.Random;
import java.lang.Math;
import java.util.ArrayList;
import java.util.Arrays;
import java.io.File;
import java.util.Scanner;
import java.lang.Math;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

// NOTE: 启动时在程序第一行输入jc, 即可进入


// i for (inclusive), e for exclusive
class RandomTest{
    public static int[] getKHT(){
		int k=0;
		int h = 0;
		int[] arr_headkh = {0};
		while (k==0 || h==0){ // k, h 0(e)
		Random r1 = new Random(1000);
		Random r2 = new Random(2000);		
		k=r1.nextInt((int)Math.pow(10, 4)+1);// k: 0(i) to 10**4(i)
		h=r2.nextInt(k+1);// h: 0(i) to k(i)
		arr_headkh = new int[k+2]; // 头部是kh
		}
		arr_headkh[0]=k;
		arr_headkh[1]=h;
		for(int i=2;i<k+2;i++){ // 开头占了2人, 结尾就空出两个位子
			Random ri=new Random(2001+i); // prevent same seeds
			arr_headkh[i]=ri.nextInt(Integer.MAX_VALUE); // 0(i) to Integer.MAX_VALUE(i)
			//`https://web.archive.org/web/20220605133421/https://docs.oracle.com/javase/6/docs/api/java/util/Random.html`#nextInt%28int%29
		}
		return arr_headkh;
    }
}
public class AS1Codes_117010155 extends RandomTest {
//	private static int[] arr;

	public static int getHthMin(int[] arr, int h, int low, int high) {
		if (low>high) {
			return -1;
		}
		int i,j,temp,minResult;
		i=low;
		j=high;
		int pivot=arr[low];
		while(i<j) {
			while(pivot<=arr[j] && i<j) {
				j-=1;
			}
			while (pivot>=arr[i] && i<j) {
				i+=1;
			}
			if(i<j) {
				temp=arr[j];
				arr[j]=arr[i];
				arr[i]=temp;
			}
		}
		arr[low]=arr[i];
		arr[i]=pivot;
		if (i==h-1) {
			return arr[i];
		} else if (i<h-1) {
			minResult=getHthMin(arr, h, i+1, arr.length-1);
		} else {
			minResult=getHthMin(arr,h,0,i-1);
		}
		return minResult;
	}
	
	
	public static boolean isPrime(int n) {
		if (n<=1)
			return false;
		if (n<=3)
			return true;
		if (n%2==0 || n%3==0)
			return false;
		int sqrt_n=(int) Math.sqrt(n);
		for (int i=5; i<=sqrt_n;i=i+6) {
			if(n%i==0 || n%(i+2)==0) {
				return false;
			}
		}
		return true;
	}
	
	// Driver program to test above methods  
    public static void main(String[] args) 
    { 
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	String str1=null,str2=null;
    	int k=0;
    	int h=0;
    	try {
    		str1=br.readLine();
    		str2=br.readLine();
    	} catch(IOException e) {
    		e.printStackTrace();
    	}
    	if(str1!=null && !str1.equals("jc")) {
    	String[] str1_list=str1.split(" ");
    	k=Integer.valueOf(str1_list[0]);
    	h=Integer.valueOf(str1_list[1]);
    	int[] arr=new int[k];
    	if (str2 != null) {
    		String[] str2_list=str2.split(" ");
    		for(int i=0; i<k; i++) {
    			arr[i]=Integer.valueOf(str2_list[i]);
    		}
    	}
	        int h_small=getHthMin(arr, h, 0,k-1);
	        int h_large=getHthMin(arr, k-h-1, 0, k-1); // 4个元素来看, 第2大就是第3小.因此h+x=length-1
	        int m=h_large-h_small;
	        boolean primeOrNot=isPrime(Math.abs(m));
	        if (primeOrNot)
	        	System.out.println("YES");
	        else
	        	System.out.println("NO");
	        System.out.println(m);
	    } 	
    	else if(str1.equals("jc")){// jc=jiancha
			System.out.println(str1);
			int[] kht=getKHT();
			k=kht[0];
			h=kht[1];
			int[] arr=Arrays.copyOfRange(kht,2,kht.length);
	        int h_small=getHthMin(arr, h, 0,k-1);
	        int h_large=getHthMin(arr, k-h-1, 0, k-1); // 4个元素来看, 第2大就是第3小.因此h-x=length-1
	        int m=h_large-h_small;
	        boolean primeOrNot=isPrime(Math.abs(m));
	        if (primeOrNot)
	        	System.out.println("YES");
	        else
	        	System.out.println("NO");
	        System.out.println(m);
	    } 
		}
}
```