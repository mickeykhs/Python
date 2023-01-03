package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JOptionPane;
import javax.swing.SwingConstants;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JButton btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btnCall;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 256, 308);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(23, 26, 179, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		btn1 = new JButton("1");
		
//				JButton b = (JButton) e.getSource();
//				System.out.println("e: " + b.getText());
		btn1.setBounds(23, 57, 50, 29);
		contentPane.add(btn1);
		
		btn2 = new JButton("2");
//		btn2.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				myclick(e);
//			}
//		});
		btn2.setBounds(85, 57, 50, 29);
		contentPane.add(btn2);
		
		btn3 = new JButton("3");
//		btn3.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				myclick(e);
//			}
//		});
		btn3.setBounds(147, 57, 50, 29);
		contentPane.add(btn3);
		
		btn4 = new JButton("4");
		btn4.setBounds(23, 90, 50, 29);
		contentPane.add(btn4);
		
		btn5 = new JButton("5");
//		btn5.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				myclick(e);
//			}
//		});
		btn5.setBounds(85, 90, 50, 29);
		contentPane.add(btn5);
		
		btn6 = new JButton("6");
//		btn6.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				myclick(e);
//			}
//		});
		btn6.setBounds(147, 90, 50, 29);
		contentPane.add(btn6);
		
		btn7 = new JButton("7");
//		btn7.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				myclick(e);
//			}
//		});
		btn7.setBounds(23, 129, 50, 29);
		contentPane.add(btn7);
		
		btn8 = new JButton("8");
//		btn8.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				myclick(e);
//			}
//		});
		btn8.setBounds(85, 129, 50, 29);
		contentPane.add(btn8);
		
		btn9 = new JButton("9");
//		btn9.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				myclick(e);
//			}
//		});
		btn9.setBounds(147, 129, 50, 29);
		contentPane.add(btn9);
		
		btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(e);
			}
		});
		btn0.setBounds(23, 168, 50, 32);
		contentPane.add(btn0);
		
		btnCall = new JButton("CALL");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				mycall();
			}
		});
		btnCall.setBounds(85, 168, 117, 32);
		contentPane.add(btnCall);
	
	btn1.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
	btn2.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
	btn3.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
	btn4.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
	btn5.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
	
	btn6.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
	btn7.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
	btn8.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
	btn9.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
	btn0.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});}
	
	public void myclick(MouseEvent e) {
		JButton b = (JButton) e.getSource();
		String str_new = b.getText();
		String str_old = tf.getText();
		tf.setText(str_old+str_new);
	}
	
	public void mycall() {
		JOptionPane.showMessageDialog(null, "CALLING : " +tf.getText(), "전화번호", JOptionPane.INFORMATION_MESSAGE);
	}

}
