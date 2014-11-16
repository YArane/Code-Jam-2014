import java.util.*;
public class MatrixMath{
	public int[][] addMatrices(ArrayList<int[][]> element){
		int[][] result = new int[element.get(0).length][element.get(0)[0].length];
		for(int i=0;i<element.size();i++){
			for(int j=0;j<element.get(i).length;j++){
				for( int k=0;k<element.get(i)[j].length;k++){
					result[j][k] = result[j][k] + element.get(i)[j][k];
				}
			}
		}
		return result;
	}
	
	public int[][] subtractMatrices(ArrayList<int[][]> element){
		int[][] result = new int[element.get(0).length][element.get(0)[0].length];
		for(int i=0;i<element.size();i++){
			for(int j=0;j<element.get(i).length;j++){
				for( int k=0;k<element.get(i)[j].length;k++){
					if(i==0){
						result[j][k] = result[j][k] + element.get(i)[j][k];	
					}else{
						result[j][k] = result[j][k] - element.get(i)[j][k];
					}
				}
			}
		}
		return result;
	}

	public int[][] multiplyMatrices(int[][] a, int[][] b){
		System.out.println(b.length + " , " + a[0].length);
		int[][] result = new int[b.length][a[0].length];
		for(int i=0;i<a[0].length;i++){
			for(int j=0;j<b.length;j++){
				result[i][j] = dotProduct(transpose(a)[i], b[j], b[j]);
				System.out.println(result[i][j]);
			}
		}
		return result;
	}

	public int[][] transpose(int[][] a){
		int[][] result = new int[a[0].length][a.length];
		for(int i=0;i<a[0].length;i++){
			for(int j=0;j<a.length;j++){
				result[i][j] = a[j][i];
			}
		}
		return result;
	}

	public int dotProduct(int[] a, int[] b, int[] c){
		int result = 0;
		for(int i=0;i<b.length;i++){
			System.out.println(a[i] + " * " + b[i]);
			result = result + a[i]*b[i];
		}
		return result;
	}

	public int[][] reduceMatrix(int[][] element){
		return new int[0][0];
	}

	public int[][] rowReduceMatrix(int[][] element){
		return new int[0][0];
	}

	public int[][] diagonalizeMatrix(int[][] element){
		return new int[0][0];
	}

	public int[][] inverseMatrix(int[][] element){
		return new int[0][0];
	}

	public int[][] calculateDeterminant(int[][] element){
		return new int[0][0];
	}

	public int[][] lUFactorizeMatrix(int[][] element){
		return new int[0][0];
	}

}