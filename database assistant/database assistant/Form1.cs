using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace database_assistant
{
    public partial class Form1 : Form
    {
        Image file;
        public string ss;
        //output of segmantation
        string filename = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput.txt";
        //string filename = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\ER.txt";
        public Form1()
        {
            InitializeComponent();
            txtFileRead();
            //InitializeComponent();
            //EditButton.Visible = false;
            // metroTile.Visible = false;
            //txtFileRead();
            //SAVE.Visible = false;
            //delitephotos();
            //textcontentload();
            //readtxtfile();
        }

        ///textfileread andwrite///////////////////////////

        public void txtFileRead()
        {

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




        public void readtxtfile()
        {
            List<string> lines = File.ReadLines("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput.txt").ToList();

            foreach (string current in lines)
            {
                richTextBox1.Text += current;
            }

        }

        public void textFileWrite()
        {
            try
            {
                using (StreamWriter writetext = new StreamWriter("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\voiceinput.txt"))
                {
                    writetext.WriteLine(richTextBox1.Text);
                }
            }
            catch (Exception)
            {

            }
        }

        private void delitephotos()
        {
            string[] files = System.IO.Directory.GetFiles(@"D:\sliit\4th year\CDAP\proj_workspace\developsystem\database assistant\database assistant\bin\Debug", "*.jpg");

            foreach (string file in files)
            {
                System.IO.File.Delete(file);
            }
        }




        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            try
            {

                Process process = Process.Start(@"D:\sliit\4th year\CDAP\proj_workspace\developsystem\database assistant\pyscript\voice\dist\speech2text1\speech2text1.exe");
                int id = process.Id;
                Process tempProc = Process.GetProcessById(id);
                this.Visible = true;
                tempProc.WaitForExit();
                this.Visible = true;




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }

           
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Process process = Process.Start(@"D:\sliit\4th year\CDAP\proj_workspace\developsystem\database assistant\exefile\spellchecker\SpellCheck.exe");
            int id = process.Id;
            Process tempProc = Process.GetProcessById(id);
            this.Visible = true;
            tempProc.WaitForExit();
            this.Visible = true;



        }


        public void textFileWrite1()
        {
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

        private void button3_Click(object sender, EventArgs e)
        {

            textFileWrite1();
            richTextBox1.Clear();
        
            txtFileRead();
            //textFileWrite();
        }

        private void button4_Click(object sender, EventArgs e)
        {



            try
            {

                Process process = Process.Start(@"D:\sliit\4th year\CDAP\proj_workspace\developsystem\database assistant\exefile\Rmgdrramanayaka\dist\segmrnt913_workingbacic\segmrnt913_workingbacic.exe");
                int id = process.Id;
                Process tempProc = Process.GetProcessById(id);
                this.Visible = true;
                tempProc.WaitForExit();
                this.Visible = true;




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }


            try
            {
                string path = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\exefile\\damidu\\ermaker_danesh";
                Process process = new Process();
                process.EnableRaisingEvents = false;
                process.StartInfo.FileName = "java.exe";
                process.StartInfo.Arguments = "-jar " + '"' + path + "\\ErMaker.jar";
                process.Start();




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            /////mapdb//
            try
            {

                Process process = Process.Start(@"D:\sliit\4th year\CDAP\proj_workspace\gihan_map\dist\segmrnt913_workingbacic\segmrnt913_workingbacic.exe");
                int id = process.Id;
                Process tempProc = Process.GetProcessById(id);
                this.Visible = true;
                tempProc.WaitForExit();
                this.Visible = true;




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }










            //runremap

            try
            {
                string path = "E:\\rescerch\\Remapping\\exe";
                Process process = new Process();
                process.EnableRaisingEvents = false;
                process.StartInfo.FileName = "java.exe";
                process.StartInfo.Arguments = "-jar " + '"' + path + "\\Remapping.jar";
                process.Start();




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }
            /////////////////////////////////////////////////////////////////////////////////////////////////////////









            //dbcon
            try
            {
                string path = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug";
                Process process = new Process();
                process.EnableRaisingEvents = false;
                process.StartInfo.FileName = "java.exe";
                process.StartInfo.Arguments = "-jar " + '"' + path + "\\Mainclass.jar";
                process.Start();




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }


        }

        public void textcontentload()
        {
            string filename = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\ConsoleApplication2\\exefiles\\spech2txt\\dist\\Script\\sample.txt";
            int delayTimeMilliseconds = 5000;

            // Note: File.ReadLines() defaults to UTF8.

            foreach (string line in File.ReadLines(filename))
            {
                try
                {
                    OpenFileDialog openFile1 = new OpenFileDialog();
                    openFile1.Filter = "Text Files|*.txt";
                    if (openFile1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
                    {

                        string[] readText = File.ReadAllLines(openFile1.FileName);
                        richTextBox1.LoadFile(openFile1.FileName, RichTextBoxStreamType.PlainText);
                    }

                }
                catch (Exception)
                {


                }




            }
        }







        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            TextBox richTextBox1 = new TextBox();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            string javacPathName = @"C:\Program Files\Java\jdk1.8.0_161";
            string javaFilePathName = @"E:\rescerch\Remapping\src\remapping\MainClass.java";
            string commandLineOptions = "";

            richTextBox1.Clear();
            richTextBox1.Clear();
            txtFileRead();


        }

        private void button7_Click(object sender, EventArgs e)

        {
           
            SaveFileDialog f = new SaveFileDialog();

            if (f.ShowDialog() == DialogResult.OK)
            {

                file.Save("D:\\sliit\\4th year\\CDAP\\proj_workspace\\developsystem\\database assistant\\database assistant\\bin\\Debug\\ER.txt");
            }

            SAVE.Visible = true;




        }

        private void button7_Click_1(object sender, EventArgs e)
        {
            OpenFileDialog f = new OpenFileDialog();
            f.Filter = "JPG(*.JPG) |*.jpg";

            if (f.ShowDialog() == DialogResult.OK)
            {

                file = Image.FromFile(f.FileName);
                pictureBox1.Image = file;

            }
        }

        private void button9_Click(object sender, EventArgs e)
        {

            try
            {
                                                    //D:\sliit\4th year\CDAP\proj_workspace\developsystem\database assistant\pyscript\chathura\dist\main
                Process process = Process.Start(@"D:\sliit\4th year\CDAP\proj_workspace\developsystem\database assistant\pyscript\chathura\dist\main\main.exe");
                int id = process.Id;
                Process tempProc = Process.GetProcessById(id);
                this.Visible = true;
                tempProc.WaitForExit();
                this.Visible = true;




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }


            try
            {
                string path = "C:\\Users\\DANESH\\Desktop\\damidu\\ErMaker\\dist";
                Process process = new Process();
                process.EnableRaisingEvents = false;
                process.StartInfo.FileName = "java.exe";
                process.StartInfo.Arguments = "-jar " + '"' + path + "\\ErMaker.jar";
                process.Start();




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }















        }

        private void button8_Click(object sender, EventArgs e)
        {


            Form2 frm2 = new Form2();
            {
                frm2.ShowDialog();
            }



            /////////1//////////////////
            try
            {
                string path = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\gihnfinal\\exe\\new1";
                Process process = new Process();
                process.EnableRaisingEvents = false;
                process.StartInfo.FileName = "java.exe";
                process.StartInfo.Arguments = "-jar " + '"' + path + "\\ReadingTxt1.jar";
                process.Start();




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }

            ///////////////2//////////////////////////////
            try
            {
                string path = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\gihnfinal\\exe\\new2";
                Process process = new Process();
                process.EnableRaisingEvents = false;
                process.StartInfo.FileName = "java.exe";
                process.StartInfo.Arguments = "-jar " + '"' + path + "\\split2nf.jar";
                process.Start();




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }

            /////////////////////////3////////////////////////////////
            try
            {
                string path = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\gihnfinal\\exe\\new3";
                Process process = new Process();
                process.EnableRaisingEvents = false;
                process.StartInfo.FileName = "java.exe";
                process.StartInfo.Arguments = "-jar " + '"' + path + "\\DisplayMultiValue.jar";
                process.Start();




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }
            ///////////////////////////4/////////////////////////////////
            try
            {
                string path = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\gihnfinal\\exe\\new4";
                Process process = new Process();
                process.EnableRaisingEvents = false;
                process.StartInfo.FileName = "java.exe";
                process.StartInfo.Arguments = "-jar " + '"' + path + "\\DisplayRepeatValue.jar";
                process.Start();




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }
            /////////////////////////////5/////////////////////////////////////////////
            try
            {
                string path = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\gihnfinal\\exe\\new5";
                Process process = new Process();
                process.EnableRaisingEvents = false;
                process.StartInfo.FileName = "java.exe";
                process.StartInfo.Arguments = "-jar " + '"' + path + "\\DisplaySecondNF.jar";
                process.Start();




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }

            ////////////////////////////////6//////////////////////////////////////////////////

            try
            {
                string path = "D:\\sliit\\4th year\\CDAP\\proj_workspace\\gihnfinal\\exe\\new6";
                Process process = new Process();
                process.EnableRaisingEvents = false;
                process.StartInfo.FileName = "java.exe";
                process.StartInfo.Arguments = "-jar " + '"' + path + "\\DbConnection.jar";
                process.Start();




            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());

            }
            ///////////////////////////////////////7/////////////////////////////////////////////
          




























        }

        private void button10_Click(object sender, EventArgs e)
        {
            Form2 frm2 = new Form2();
            {
                frm2.ShowDialog();
            }
        }
    
    }
}
