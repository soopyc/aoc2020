package boblovespi.adventoccode;

import java.io.*;
import java.util.Random;

public class Day3
{
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new FileReader("day3test.txt"));
		String[] trees = new String[101];

		int c31 = 0;
		int c11 = 0;
		int c51 = 0;
		int c71 = 0;
		int c12 = 0;
		for (int i = 0; i < 101; i++)
		{
			trees[i] = br.readLine();
			if (trees[i].charAt(3 * i % trees[i].length()) == '#')
				c31++;
			if (trees[i].charAt(5 * i % trees[i].length()) == '#')
				c51++;
			if (trees[i].charAt(7 * i % trees[i].length()) == '#')
				c71++;
			if (trees[i].charAt(i % trees[i].length()) == '#')
				c11++;
			if (i % 2 == 0 && trees[i].charAt(i / 2 % trees[i].length()) == '#')
				c12++;
		}
		System.out.println(c31);
		System.out.println(c31 * c11 * c12 * c51 * c71);

		PrintWriter pw = new PrintWriter(new FileWriter("day3test.txt"));
		pw.println("...............................");
		Random r = new Random(100);
		for (int i = 0; i < 100; i++)
		{
			for (int j = 0; j < 31; j++)
			{
				if (r.nextDouble() > 0.8)
					pw.print("#");
				else
					pw.print(".");
			}
			if (i != 99)
				pw.println();
		}
		pw.flush();
	}
}
