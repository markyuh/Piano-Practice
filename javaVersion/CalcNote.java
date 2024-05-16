package PianoGame.javaVersion;
import java.awt.Rectangle;
import java.util.HashMap;
public class CalcNote {
    public static HashMap<Rectangle, String> noteMap = new HashMap<>();
    int x;
    int y;
    public CalcNote(int x, int y){
        this.x = x;
        this.y = y;
    }
    public static void init() {
        noteMap.put(new Rectangle(177, 463, 23, 220),"A");
        noteMap.put(new Rectangle(200, 592, 12, 88), "A");
        noteMap.put(new Rectangle(201, 462, 23, 126),"A#");
        noteMap.put(new Rectangle(214, 592, 12, 88),"B");
        noteMap.put(new Rectangle(226, 462, 23, 218),"B");
        noteMap.put(new Rectangle(252, 462, 21, 218),"C");
        noteMap.put(new Rectangle(270, 589, 16, 92),"C");
        noteMap.put(new Rectangle(271, 462, 24, 127),"C#");
        noteMap.put(new Rectangle(288, 589, 8, 92),"D");
        noteMap.put(new Rectangle(295, 463, 19, 219),"D");
        noteMap.put(new Rectangle(313, 589, 10, 92),"D");
        noteMap.put(new Rectangle(315, 462, 23, 128),"D#");
        noteMap.put(new Rectangle(324, 590, 15, 91),"E");
        noteMap.put(new Rectangle(339, 462, 21, 219),"E");
        noteMap.put(new Rectangle(361, 462, 21, 220),"F");
        noteMap.put(new Rectangle(380, 590, 17, 92),"F");
        noteMap.put(new Rectangle(382, 463, 24, 127),"F#");
        noteMap.put(new Rectangle(400, 591, 5, 89),"G");
        noteMap.put(new Rectangle(406, 463, 16, 219),"G");
        noteMap.put(new Rectangle(422, 590, 12, 91),"G");
        noteMap.put(new Rectangle(423, 462, 23, 129),"G#");
        noteMap.put(new Rectangle(436, 592, 10, 89),"A");
        noteMap.put(new Rectangle(448, 463, 15, 219),"A");
        noteMap.put(new Rectangle(462, 589, 10, 91), "A");
        noteMap.put(new Rectangle(472, 462, 23, 126),"A#");
        noteMap.put(new Rectangle(472, 590, 15, 90),"B");
        noteMap.put(new Rectangle(488, 462, 20, 219),"B");
        noteMap.put(new Rectangle(510, 463, 20, 220),"C");
        noteMap.put(new Rectangle(530, 591, 15, 90),"C");
        noteMap.put(new Rectangle(530, 463, 23, 128),"C#");
        noteMap.put(new Rectangle(546, 590, 8, 89),"D");
        noteMap.put(new Rectangle(554, 463, 19, 220),"D");
        noteMap.put(new Rectangle(573, 590, 8, 91),"D");
        noteMap.put(new Rectangle(574, 463, 24, 127),"D#");
        noteMap.put(new Rectangle(584, 590, 14, 91),"E");
        noteMap.put(new Rectangle(598, 462, 21, 220),"E");
        noteMap.put(new Rectangle(621, 462, 19, 220),"F");
        noteMap.put(new Rectangle(639, 590, 18, 91),"F");
        noteMap.put(new Rectangle(640, 463, 24, 127),"F#");
        noteMap.put(new Rectangle(657, 590, 8, 90),"G");
        noteMap.put(new Rectangle(665, 463, 16, 220),"G");
        noteMap.put(new Rectangle(681, 590, 12, 91),"G");
        noteMap.put(new Rectangle(681, 463, 24, 128),"G#");
        noteMap.put(new Rectangle(695, 591, 12, 91),"A");
        noteMap.put(new Rectangle(706, 462, 16, 221),"A");
        noteMap.put(new Rectangle(721, 589, 8, 92), "A");
        noteMap.put(new Rectangle(722, 463, 24, 128),"A#");
        noteMap.put(new Rectangle(730, 591, 16, 91),"B");
        noteMap.put(new Rectangle(747, 463, 19, 219),"B");
        noteMap.put(new Rectangle(768, 463, 19, 219),"C");
        noteMap.put(new Rectangle(787, 591, 16, 91),"C");
        noteMap.put(new Rectangle(787, 463, 25, 128),"C#");
        noteMap.put(new Rectangle(805, 592, 7, 90),"D");
        noteMap.put(new Rectangle(812, 463, 19, 220),"D");
        noteMap.put(new Rectangle(830, 590, 10, 91),"D");
        noteMap.put(new Rectangle(831, 463, 25, 127),"D#");
        noteMap.put(new Rectangle(842, 591, 13, 91),"E");
        noteMap.put(new Rectangle(856, 463, 20, 218),"E");
        noteMap.put(new Rectangle(879, 463, 19, 220),"F");
        noteMap.put(new Rectangle(897, 590, 16, 91),"F");
        noteMap.put(new Rectangle(898, 463, 25, 127),"F#");
        noteMap.put(new Rectangle(915, 592, 8, 90),"G");
        noteMap.put(new Rectangle(923, 463, 17, 219),"G");
        noteMap.put(new Rectangle(939, 590, 11, 91),"G");
        noteMap.put(new Rectangle(939, 463, 24, 127),"G#");
        noteMap.put(new Rectangle(953, 592, 11, 90),"A");
        noteMap.put(new Rectangle(964, 463, 16, 218),"A");
        noteMap.put(new Rectangle(979, 589, 9, 91), "A");
        noteMap.put(new Rectangle(979, 463, 25, 127),"A#");
        noteMap.put(new Rectangle(990, 592, 14, 90),"B");
        noteMap.put(new Rectangle(1005, 463, 19, 219),"B");
        



    }
}
