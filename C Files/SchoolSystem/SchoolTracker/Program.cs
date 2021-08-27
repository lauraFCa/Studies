using System;
using System.Collections.Generic;

namespace SchoolTracker
{
    enum School
    {
        //by default, ENUM starts with 0 and so on
        Hogwarts,
        Harvard,
        MIT
    }

    class Program
    {
        static List<Student> students  = new List<Student>();
        static void Main(string[] args)
        {
            Logger.Log("Tracker started", priority: 0);

            PayRoll payroll = new PayRoll();
            payroll.PayAll();

            var adding = true;

            while (adding)
            {
                try
                {
                    Logger.Log("Adding new student");
                    var newStudent = new Student();

                    newStudent.Name = Util.Console.Ask("Student Name: ");

                    newStudent.Grade = Util.Console.AskInt("Student Grade: ");

                    newStudent.school = (School) Util.Console.AskInt("School Name (type number): " +
                        "\n0 - Hogwarts \n1 - Harvard \n2 - MIT \n");

                    newStudent.Birthday = Util.Console.Ask("Student Birthday: ");

                    newStudent.Address = Util.Console.Ask("Student Address: ");

                    newStudent.phone = Util.Console.AskInt("Student Phone Number: ");

                    students.Add(newStudent);
                    Student.Count++;
                    Console.WriteLine("Student Count: {0}", Student.Count);

                    Console.WriteLine("Add another? y/n");

                    if (Console.ReadLine() != "y")
                        adding = false;
                }
                catch (FormatException msg)
                {
                    Console.WriteLine(msg.Message);
                }
                catch (Exception)
                {
                    Console.WriteLine("Error adding student, Please try again");
                }
            }

            ShowGrade("Tom");

            foreach (var student in students)
            {
                Console.WriteLine("Name: {0}, Grade: {1}", student.Name, student.Grade);
            }
            Import();
            Export();

            var someObj = new { name = "alex", age = 54 }; //data anonymous time
        }

        static void Import()
        {
            var importedStudent = new Student("Jenny", 86, "birthday", "address", 123456);
            Console.WriteLine("Imported: \n" + importedStudent.Name);
        }

        static void Export()
        {
            foreach (var item in students)
            {
                switch (item.school)
                {
                    case School.Hogwarts:
                        Console.WriteLine("Export Hogwarts");
                        break;

                    case School.Harvard:
                        Console.WriteLine("Export Harvard");
                        break;

                    case School.MIT:
                        Console.WriteLine("Export MIT");
                        break;

                    default:
                        Console.WriteLine("no export");
                        break;
                }
            }
        }
    
        static void ShowGrade(string name)
        {
            var found = students.Find(student => student.Name == name);
            Console.WriteLine("{0}'s Grade: {1}", found.Name, found.Grade);
        }
    }

    class Member
    {
        public string Name { get; set; }  // auto implemented property
        public string Address { get; set; }
        public int phone { get; set; }
    }

    class Student : Member
    {
        static public int Count = 0;

        public int Grade { get; set; }
        public string Birthday { get; set; }
        public School school { get; set; }

        public Student()
        {

        }

        public Student(string name, int grade, string birthday, string address, int phone)
        {
            Name = name;
            Grade = grade;
            Birthday = birthday;
            Address = address;
            phone = phone;
        }
    }
}
