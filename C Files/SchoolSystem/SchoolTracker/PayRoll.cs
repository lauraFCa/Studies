using System;
using System.Collections.Generic;
using System.Text;

namespace SchoolTracker
{
    interface IPayee
    {
        void Pay();
    }
    class PayRoll
    {
        //Teacher teacher1 = new Teacher();
        //Teacher teacher2 = new Teacher();
        //Principal principal1 = new Principal();

        List<IPayee> payees = new List<IPayee>();

        public PayRoll()
        {
            payees.Add(new Teacher());
            payees.Add(new Teacher());
            payees.Add(new Principal());

            Logger.Log("Payroll started", "PayRoll");
        }

        public void PayAll()
        {
            //teacher1.Pay();
            //teacher2.Pay();
            //principal1.Pay();

            foreach (var payee in payees)
            {
                payee.Pay();
            }

            Logger.Log("PayAll completed", "PayRoll");
        }
    }
}
