package PianoGame.javaVersion;
import javax.swing.JFrame;

public class GameFrame extends JFrame{
    
    GameFrame(){
        //here we are creating a new window(panel) to pop up 
        this.add(new GamePanel());
        this.setTitle("Sheet Note");//title of the panel
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//program exited when closed
        this.setResizable(false);//doesn't allow for resizing of the frame
        this.pack();//fits frame snugly around all components added to frame
        this.setVisible(true);//makes the panel visible
        this.setLocationRelativeTo(null);//makes the panel appear in the middle of the screenx


    }

}