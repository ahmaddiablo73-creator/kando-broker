using System;
using System.IO;
class Kando {
    static void Main() {
        string logPath = "kando_response.log";
        File.WriteAllText(logPath, ">>> هسته [فعال]: ارتباطِ فایل برقرار شد." + Environment.NewLine);
        while(true) {
            string input = Console.ReadLine();
            if(input == "exit") break;
            File.AppendAllText(logPath, ">>> کاندو: دریافت شد: " + input + Environment.NewLine);
        }
    }
}
