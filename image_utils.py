import cv2
import numpy as np

from PIL import Image
import PIL.ImageOps

import SimpleITK as sitk
from sklearn.feature_extraction import image

from scipy import sparse

# convert a numpy array to image
def array_to_img(filename):

  img = cv2.imread(filename)
  array = np.array(img)
  array = np.where(array == 0, 255, array) #change all pixels with 0 intensity to 255 intensity
  im = Image.fromarray(array)
  # im.save("out/" + filename) #save image
  
  return img

# invert pixel intensity of a grayscale image
def invert_img_in_grayscale(filename):

  img = Image.open(filename)
  inverted_image = PIL.ImageOps.invert(img)
  #inverted_image.save("out/" filename1) #save image
  
  return inverted_image

#convert a 3d-image to an undirected graph
def get_graph_from_3d_image(filename):

  img3d = sitk.ReadImage(filename)
  array = sitk.GetArrayFromImage(img3d)
  graph = image.img_to_graph(array)
  
  return graph
  
#get a adjacency matrix from a graph
def get_adjacency_matrix_from_graph(graph):

  adj_matrix = graph.toarray()
  
  return adj_matrix

#get a compressed sparse row matrix from adjacency matrix
def get_sparse_matrix_by_row(adjacency_matrix):

    data_csr = sparse.csr_matrix(adjacency_matrix)
    
    return data_csr
  
#get a compressed sparse column matrix from adjacency matrix
def get_sparse_matrix_by_column(adjacency_matrix):

    data_csc = sparse.csc_matrix(adjacency_matrix)
    
    return data_csc
