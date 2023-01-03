package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tfFirst;
	private JTextField tfLast;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 323, 480);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblFirst = new JLabel("첫별수");
		lblFirst.setBounds(37, 31, 57, 15);
		contentPane.add(lblFirst);
		
		JLabel lblLast = new JLabel("끝별수");
		lblLast.setBounds(37, 78, 57, 15);
		contentPane.add(lblLast);
		
		tfFirst = new JTextField();
		tfFirst.setBounds(130, 28, 116, 21);
		contentPane.add(tfFirst);
		tfFirst.setColumns(10);
		
		tfLast = new JTextField();
		tfLast.setColumns(10);
		tfLast.setBounds(130, 75, 116, 21);
		contentPane.add(tfLast);
		
		JButton btn = new JButton("별출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(37, 113, 209, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(37, 157, 209, 259);
		contentPane.add(ta);
	}
	
	public String drawStar(int cnt) {
		String ret = "";
		for(int i=0; i<cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		return ret;
	}
	
	public void myclick() {
		int fir = Integer.parseInt(tfFirst.getText());
		int las = Integer.parseInt(tfLast.getText());
		
		String txt = "";
		for(int i=fir; i<=las; i++) {
			txt += drawStar(i);
		}
		ta.setText(txt);
		
//		txt += drawStar(3);   ret= ***
//		txt += drawStar(5);	  ret= *****
		
//		String star = "*";
//		String one = tfFirst.getText();
//		for(int i=fir; i<=las; i++) {
//			for(int j=fir; i>=j; j++) {
//				txt += star;
//			}
//			txt += "\n";
//		}
//		ta.setText(txt);
	}

}
