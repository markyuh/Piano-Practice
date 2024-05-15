package PianoGame;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.EmptyBorder;//might be able to remove
import java.util.Random;
import javax.swing.Timer;

public class GamePanel extends JPanel implements ActionListener {
    static final int SCREEN_WIDTH = 1200;
    static final int SCREEN_HEIGHT = 700;
    private Image checkMarkImage;
    private Image xMarkImage;
    boolean running = false;
    Random rand;
    int noteNum;
    ImageIcon notePic;
    JLabel noteLabel;
    private boolean showFeedback = false;
    private Image feedbackImage;
    private static final int FEEDBACK_X = 800;
    private static final int FEEDBACK_Y = 100;
    private String lastClickedNote = "";
    private boolean wasLastNoteCorrect = false;
    private JButton rollButton;

    GamePanel() {
        this.setLayout(null);
        rand = new Random();
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
        this.setBackground(Color.black);
        this.setFocusable(true);
        this.addMouseListener(new MyMouseAdapter());

        CalcNote.init();

        JLabel keyboardLabel = makeKeyboard();
        keyboardLabel.setBounds(175, 460, 850, 240);
        this.add(keyboardLabel);

        JButton rollButton = makeRoll();
        rollButton.setBounds(550, 360, 117, 29);
        this.add(rollButton);

        JLabel noteLabel = makeNote();
        noteLabel.setBounds(450, 40, 300, 300);
        this.add(noteLabel);

        ImageIcon checkMarkIcon = new ImageIcon(getClass().getResource("graphics/CheckMark.png"));
        checkMarkImage = checkMarkIcon.getImage().getScaledInstance(300, 300, Image.SCALE_SMOOTH);
        ImageIcon xMarkIcon = new ImageIcon(getClass().getResource("graphics/x.png"));
        xMarkImage = xMarkIcon.getImage().getScaledInstance(300, 300, Image.SCALE_SMOOTH);

    }

    public void startGame() {
        running = true;
    }

    public JLabel makeKeyboard() {
        ImageIcon originalImage = new ImageIcon(getClass().getResource("graphics/Keyboard.png"));
        Image scalingImage = originalImage.getImage().getScaledInstance(850, 240, Image.SCALE_SMOOTH);
        ImageIcon image = new ImageIcon(scalingImage);
        JLabel displayField = new JLabel(image);
        displayField.setBorder(new EmptyBorder(0, 0, 40, 0));

        return displayField;
    }

    public JButton makeRoll() {
        rollButton = new JButton("Click to Start");
        rollButton.setBounds(550, 360, 117, 29);
        rollButton.addActionListener(this);
        return rollButton;
    }

    public JLabel makeNote() {
        noteLabel = new JLabel();
        noteLabel.setBounds(100, 200, 300, 300);
        notePic = new ImageIcon(getClass().getResource("graphics/notes/0.png"));
        Image scalingImage = notePic.getImage().getScaledInstance(300, 300, Image.SCALE_SMOOTH);
        ImageIcon scaledIcon = new ImageIcon(scalingImage);
        noteLabel.setIcon(scaledIcon);
        return noteLabel;
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        draw(g);
        if (showFeedback && feedbackImage != null) {
            g.drawImage(feedbackImage, FEEDBACK_X, FEEDBACK_Y, this);
            if (wasLastNoteCorrect) {
                g.setColor(Color.GREEN);
            } else {
                g.setColor(Color.RED);
            }
            g.setFont(new Font("Arial", Font.BOLD, 50));
            g.drawString(lastClickedNote, FEEDBACK_X + 135, FEEDBACK_Y - 20);
        }
        }
    

    public void draw(Graphics g) {
        g.setFont(new Font("Ink Free", Font.BOLD, 30));
        FontMetrics metrics = getFontMetrics(g.getFont());
        g.drawString("Score: ", (SCREEN_WIDTH - metrics.stringWidth("Score :")) / 2, g.getFont().getSize());
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == rollButton) {
            if (!running) {
                running = true;
                rollButton.setVisible(false); // Make button invisible after click
    
                // Move the game starting logic here
                rand = new Random();
                noteNum = rand.nextInt(17) + 1; // Assume you have 17 different notes
                notePic = new ImageIcon(getClass().getResource("graphics/notes/" + noteNum + ".png"));
                Image scalingImage = notePic.getImage().getScaledInstance(300, 300, Image.SCALE_SMOOTH);
                ImageIcon scaledIcon = new ImageIcon(scalingImage);
                noteLabel.setIcon(scaledIcon);
                noteLabel.revalidate();
                repaint();
            }
        }
        // }
        // rand = new Random();
        // noteNum = rand.nextInt(17) + 1;
        // notePic = new ImageIcon(getClass().getResource("graphics/notes/" + noteNum + ".png"));
        // Image scalingImage = notePic.getImage().getScaledInstance(300, 300, Image.SCALE_SMOOTH);
        // ImageIcon scaledIcon = new ImageIcon(scalingImage);
        // noteLabel.setIcon(scaledIcon);
        // noteLabel.revalidate();
        // repaint();

    }

    public class MyMouseAdapter extends MouseAdapter {
        private Timer timer;
        public MyMouseAdapter() {
            timer = new Timer(2000, e -> reroll());
            timer.setRepeats(false);  // Ensure the timer only fires once per click
        }
    
        private void reroll() {
            noteNum = rand.nextInt(17) + 1;
            notePic = new ImageIcon(getClass().getResource("graphics/notes/" + noteNum + ".png"));
            Image scalingImage = notePic.getImage().getScaledInstance(300, 300, Image.SCALE_SMOOTH);
            ImageIcon scaledIcon = new ImageIcon(scalingImage);
            noteLabel.setIcon(scaledIcon);
            noteLabel.revalidate();
            repaint();
    
            showFeedback = false; 
        }

        @Override
        public void mousePressed(MouseEvent e) {
            int xVal = e.getX();
            int yVal = e.getY();

            for (Rectangle key : CalcNote.noteMap.keySet()) {

                if (key.contains(xVal, yVal)) {
                    String clickedNote = CalcNote.noteMap.get(key);
                    String expectedNote = NoteMap.numberToNote.get(noteNum);
                    lastClickedNote = clickedNote;
                    showFeedback = true;
                    feedbackImage = clickedNote.equals(expectedNote) ? checkMarkImage : xMarkImage;
                    wasLastNoteCorrect = clickedNote.equals(expectedNote);
                    if (clickedNote.equals(expectedNote)) {
                        System.out.println("Correct!");
                        timer.start();
                    } else {
                        System.out.println("Incorrect! Expected: " + expectedNote + ", but clicked: " + clickedNote);
                    }
                    repaint();
                    break;
                }
            }
        }
    }
}
