using System;
using System.Collections.Generic;
using System.Text;

namespace Util
{

    public static class ExtensionMethods
    {
        public static int toInt(this string value)
        {
            return int.Parse(value);
        }
    }

    class Console
    {
        static public string Ask(string question)
        {
            System.Console.Write(question);
            return System.Console.ReadLine();
        }

        // overload original function - you can use an integer or a string
        static public string Ask(int question)
        {
            System.Console.Write(question);
            return System.Console.ReadLine();
        }

        static public int AskInt(string question)
        {
            try
            {
                System.Console.Write(question);
                return System.Console.ReadLine().toInt();
                //return int.Parse(System.Console.ReadLine());
            }
            catch (Exception)
            {
                throw new FormatException("Input was not a number");
            }
        }
    }
}
