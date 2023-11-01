using System;
using System.Diagnostics;
using System.IO;

class Program
{
    static void Main()
    {
        string pythonScript = "classifier.py";
        string photoFilePath = "crow.jpg";

        ProcessStartInfo psi = new ProcessStartInfo
        {
            FileName = "python",
            Arguments = $"{pythonScript} {photoFilePath}",
            RedirectStandardOutput = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        Process pythonProcess = new Process { StartInfo = psi };
        pythonProcess.Start();

        string output = pythonProcess.StandardOutput.ReadToEnd();
        Console.WriteLine("Output from Python:");
        Console.WriteLine(output);

        pythonProcess.WaitForExit();
        pythonProcess.Close();
    }
}