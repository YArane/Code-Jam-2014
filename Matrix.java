import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Matrix{
	int[][] element;
	int columns, rows;
	JTextField[][] textField;
	//int textFieldPosition;
	
	
	public Matrix(int[][] e, int c, int r, JTextField[][] tf){
		element = e;
		columns = c;
		rows = r;
		textField = tf;
		//textFieldPosition = tfp;
	}
	public int[][] getElements(){
		return element;
	}
	public void setElements(int[][] e){
		element = e;
	}
	public int getColumns(){
		return columns;
	}
	public int getRows(){
		return rows;
	}
	public JTextField[][] getTextFields(){
		return textField;
	}
	public void setTextFields(int[][] element){
		for(int i=0;i<columns;i++){
			for(int j=0;j<rows;j++){
				textField[i][j] = new JTextField("" + element[i][j], 3);
			}
		}
	}
}