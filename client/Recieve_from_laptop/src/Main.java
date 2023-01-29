import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Main {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(52231);
            while (true) {
                Socket socket = serverSocket.accept();
                DataInputStream inputStream = new DataInputStream(socket.getInputStream());
                String message = inputStream.readUTF();
                System.out.println("Received message: " + message);
                inputStream.close();
                socket.close();
            }
//            Socket socket = new Socket("10.0.2.2", 51021);
//            DataOutputStream outputStream =new DataOutputStream(socket.getOutputStream());
//            outputStream.writeUTF("message");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
