package boblovespi.adventoccode;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Day5
{
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new FileReader("day5.txt"));
		StringTokenizer sc; // = new StringTokenizer(br.readLine());
		String binary;
		int seatRow = 0;
		int seatColumn = 0;
		int highestId = 0;
		int[] seats = new int[891];
		for (int i = 0; i < 891; i++)
		{
			binary = br.readLine();
			for (int j = 0; j < 7; j++)
			{
				if (binary.charAt(j) == 'B')
				{
					seatRow++;
				}
				seatRow *= 2;
			}
			seatRow /= 2;

			for (int j = 0; j < 3; j++)
			{
				if (binary.charAt(j + 7) == 'R')
				{
					seatColumn++;
				}
				seatColumn *= 2;
			}

			seatColumn /= 2;
			// System.out.println(seatColumn);
			// System.out.println(seatRow);

			if (seatRow * 8 + seatColumn > highestId)
				highestId = seatRow * 8 + seatColumn;
			seats[i] = seatRow * 8 + seatColumn;
			seatRow = 0;
			seatColumn = 0;
		}

		Arrays.sort(seats);
		for (int i = 1; i < seats.length; i++)
		{
			if (seats[i] - seats[i - 1] != 1)
				System.out.println(seats[i - 1] + 1);
		}

		System.out.println(highestId);
	}
}
