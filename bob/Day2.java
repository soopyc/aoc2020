package boblovespi.adventoccode;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.StringTokenizer;

public class Day2
{
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new FileReader("day2.txt"));
		StringTokenizer sc; // = new StringTokenizer(br.readLine());

		int correct = 0;
		for (int i = 0; i < 1000; i++)
		{
			sc = new StringTokenizer(br.readLine());
			String policy = sc.nextToken();
			String[] minmax = policy.split("-");
			char letter = sc.nextToken().charAt(0);
			String password = sc.nextToken();

			/*int count = 0;
			for (char c : password.toCharArray())
			{
				if (c == letter)
					count++;
			}

			if (count >= Integer.parseInt(minmax[0]) && count <= Integer.parseInt(minmax[1]))
				correct++;*/
			boolean first = password.charAt(Integer.parseInt(minmax[0]) - 1) == letter;
			boolean second = password.charAt(Integer.parseInt(minmax[1]) - 1) == letter;
			if ((first || second) && !(first && second))
				correct++;
		}
		System.out.println(correct);
	}
}
