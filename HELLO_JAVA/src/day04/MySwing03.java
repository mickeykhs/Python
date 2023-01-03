package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf01;
	private JTextField tf02;
	private JTextField tf03;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf01 = new JTextField();
		tf01.setBounds(12, 30, 53, 21);
		contentPane.add(tf01);
		tf01.setColumns(10);
		
		tf02 = new JTextField();
		tf02.setColumns(10);
		tf02.setBounds(137, 30, 53, 21);
		contentPane.add(tf02);
		
		tf03 = new JTextField();
		tf03.setColumns(10);
		tf03.setBounds(290, 30, 53, 21);
		contentPane.add(tf03);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
				// =버튼 클릭시 계산
//				int count = Integer.parseInt(tf01.getText());
//				tf01.setText(String.valueOf(count));
//				
//				int count2 = Integer.parseInt(tf02.getText());
//				tf02.setText(String.valueOf(count2));
//				
//				int count3 = count + count2;
//				tf03.setText(String.valueOf(count3));
			}
		});
		btn.setBounds(216, 29, 53, 23);
		contentPane.add(btn);
		
		JLabel lbl = new JLabel("+");
		lbl.setBounds(95, 33, 40, 15);
		contentPane.add(lbl);
	}
	
	public void myclick() {
		String a = tf01.getText();
		String b = tf02.getText();
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		int sum = aa + bb;
		
		tf03.setText(sum +"");
	}
}
