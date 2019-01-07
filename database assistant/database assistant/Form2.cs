using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace database_assistant
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
            txtFileRead();

        }



        public void txtFileRead()
        {
            string ss;
            string filename = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\mapping.txt";

            try
            {
                string[] readText = System.IO.File.ReadAllLines(filename);
                foreach (string s in readText)
                {
                    // richTextBox1.Text += s + Environment.NewLine;
                    ss = s + Environment.NewLine;
                    richTextBox1.Text += ss;
                }
            }
            catch (Exception)
            {


            }
        }




        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {

          //  textFileWrite1();
          //  richTextBox1.Clear();

           // txtFileRead();


            //File.WriteAllText(@"D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\mapping.txt";, richTextBox1.Text);
            // System.IO.File.WriteAllText(Savefiledialog1.FileName, richTextBox1.text);




            // using stream writer class
            StreamWriter sw = new StreamWriter(@"D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\mapping.txt");

            // textbox1 is richtext box

            sw.WriteLine(richTextBox1.Text);

            //close your stream
            sw.Close();





        }
        public void textFileWrite1()
        {
            string filename = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\mapping.txt";
            try
            {
                using (StreamWriter writetext = new StreamWriter(filename))
                {
                    writetext.WriteLine(richTextBox1.Text);
                }
            }
            catch (Exception)
            {

            }
        }
        private void Form2_Load(object sender, EventArgs e)
        {

        }
    }
}
