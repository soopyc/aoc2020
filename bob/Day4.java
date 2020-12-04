package boblovespi.adventoccode;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.StringTokenizer;

public class Day4
{
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new FileReader("day4.txt"));
		StringTokenizer sc; // = new StringTokenizer(br.readLine());

		int count = 0;
		boolean byr = false;
		boolean iyr = false;
		boolean eyr = false;
		boolean hgt = false;
		boolean hcl = false;
		boolean ecl = false;
		boolean pid = false;
		boolean cid = false;
		String line;

		while (br.ready())
		{
			line = br.readLine();
			if (line.isBlank())
			{
				if (byr && iyr && eyr && hgt && hcl && ecl && pid)
					count++;
				byr = false;
				iyr = false;
				eyr = false;
				hgt = false;
				hcl = false;
				ecl = false;
				pid = false;
				cid = false;
				continue;
			}
			String[] keys = line.split(" ");
			for (String key : keys)
			{
				String realKey = key.split(":")[0];
				String data = key.split(":")[1];
				if (realKey.equals("byr"))
				{
					if (data.length() == 4 && isInt(data))
					{
						int yr = Integer.parseInt(data);
						if (yr >= 1920 && yr <= 2002)
							byr = true;
					}
				}
				if (realKey.equals("iyr"))
				{
					if (data.length() == 4 && isInt(data))
					{
						int yr = Integer.parseInt(data);
						if (yr >= 2010 && yr <= 2020)
							iyr = true;
					}
				}
				if (realKey.equals("eyr"))
				{
					if (data.length() == 4 && isInt(data))
					{
						int yr = Integer.parseInt(data);
						if (yr >= 2020 && yr <= 2030)
							eyr = true;
					}
				}
				if (realKey.equals("hgt"))
				{
					String unit = data.substring(data.length() - 2);
					String substring = data.substring(0, data.length() - 2);
					if (unit.equals("cm"))
					{
						if (isInt(substring))
						{
							int yr = Integer.parseInt(substring);
							if (yr >= 150 && yr <= 193)
								hgt = true;
						}
					} else if (unit.equals("in"))
					{
						if (isInt(substring))
						{
							int yr = Integer.parseInt(substring);
							if (yr >= 59 && yr <= 76)
								hgt = true;
						}
					}
				}
				if (realKey.equals("hcl"))
				{
					if (data.matches("#[0-9a-f]{6}") && data.length() == 7)
						hcl = true;
				}
				if (realKey.equals("ecl"))
				{
					if (data.equals("amb") || data.equals("blu") || data.equals("brn") || data.equals("gry") || data.equals("grn") || data.equals("hzl") || data.equals("oth"))
						ecl = true;
				}
				if (realKey.equals("pid"))
				{
					if (data.length() == 9 && data.matches("[0-9]{9}"))
						pid = true;
				}
				if (realKey.equals("cid"))
					cid = true;
			}
		}

		System.out.println(count);
	}

	static boolean isInt(String s)
	{
		try
		{
			Integer.parseInt(s);
			return true;
		} catch (Exception e)
		{
			return false;
		}
	}
}
