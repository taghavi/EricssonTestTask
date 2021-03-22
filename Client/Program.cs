using System;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Net.NetworkInformation;
using System.IO;

namespace Client
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {                           
                var hostName = Dns.GetHostName();
                Ping pingSender = new Ping ();
                try
                {
                    PingReply reply = pingSender.Send("server_test_task");
                    if (reply.Status == IPStatus.Success)
                        {
                            hostName = "server_test_task";
                        }               
                }
                catch
                {                                   
                    hostName = Environment.GetEnvironmentVariable("MY_SERVER");
                    System.Console.WriteLine(hostName);
                }

                TcpClient tcpclnt = new TcpClient();                               
                Console.WriteLine("Hello from Client.\nConnecting...");
                tcpclnt.Connect(hostName, 9980); 
                Console.WriteLine("Connected to "+ hostName+" port 9980");
                Console.WriteLine("Here's message from server:\n");
                NetworkStream networkStream = tcpclnt.GetStream();
                while (true)
                {
                    if (tcpclnt.ReceiveBufferSize > 0)
                    {
                        var bytes = new byte[tcpclnt.ReceiveBufferSize];
                        var eh = networkStream.Read(bytes, 0, tcpclnt.ReceiveBufferSize);
                        var msg = Encoding.UTF8.GetString(bytes, 0, eh); //the message incoming
                        Console.Write(msg);
                    }
                }               
                
                var str = Console.ReadLine();              
                networkStream.Close();  
                tcpclnt.Close();
            }

            catch (Exception e)
            {
                Console.WriteLine("Error..... " + e.StackTrace+e.Message+e.InnerException);
            }
        }
    }
}
