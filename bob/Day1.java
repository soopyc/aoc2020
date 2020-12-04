package boblovespi.adventoccode;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.StringTokenizer;

public class Day1
{
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new FileReader("day1puzzle1.txt"));
		// StringTokenizer sc = new StringTokenizer(br.readLine());
		int[] nums =  new int[200];
		for (int i = 0; i < 200; i++)
		{
			nums[i] = Integer.parseInt(br.readLine());
		}

		for (int i = 0; i < 200; i++)
		{
			for (int j = 0; j < i; j++)
			{
				for (int k = 0; k < j; k++)
				{
					if (nums[j] + nums[i] + nums[k] == 2020)
						System.out.println(nums[j] * nums[i] * nums[k]);
				}
			}
		}
	}
}
