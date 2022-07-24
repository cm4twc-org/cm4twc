import numpy as np
cimport numpy as cnp

cdef extern from "dummy.h":

    void initialise_(int ny, int nx, double *state_a_m1,
                     double *state_b_m1)

    void run_(int ny, int nx, double *transfer_i, double *transfer_n,
              double *driving_a, double *parameter_a, double *state_a_m1,
              double *state_a_0, double *state_b_m1, double *state_b_0,
              double *transfer_k, double *transfer_m, double *output_x)

    void finalise_()

def initialise(cnp.ndarray[cnp.npy_float64, ndim=2] state_a_m1,
               cnp.ndarray[cnp.npy_float64, ndim=2] state_b_m1):

    cdef int ny = state_a_m1.shape[0]
    cdef int nx = state_a_m1.shape[1]

    initialise_(ny, nx, &state_a_m1[0, 0], &state_b_m1[0, 0])

def run(cnp.ndarray[cnp.npy_float64, ndim=2] transfer_i,
        cnp.ndarray[cnp.npy_float64, ndim=2] transfer_n,
        cnp.ndarray[cnp.npy_float64, ndim=2] driving_a,
        cnp.ndarray[cnp.npy_float64, ndim=2] parameter_a,
        cnp.ndarray[cnp.npy_float64, ndim=2] state_a_m1,
        cnp.ndarray[cnp.npy_float64, ndim=2] state_a_0,
        cnp.ndarray[cnp.npy_float64, ndim=2] state_b_m1,
        cnp.ndarray[cnp.npy_float64, ndim=2] state_b_0):

    cdef int ny = transfer_i.shape[0]
    cdef int nx = transfer_i.shape[1]

    cdef cnp.ndarray[cnp.npy_float64, ndim=2] transfer_k = np.zeros(
        (ny, nx), dtype=np.float64)
    cdef cnp.ndarray[cnp.npy_float64, ndim=2] transfer_m = np.zeros(
        (ny, nx), dtype=np.float64)
    cdef cnp.ndarray[cnp.npy_float64, ndim=2] output_x = np.zeros(
        (ny, nx), dtype=np.float64)

    run_(ny, nx, &transfer_i[0, 0], &transfer_n[0, 0],
         &driving_a[0, 0], &parameter_a[0, 0], &state_a_m1[0, 0],
         &state_a_0[0, 0], &state_b_m1[0, 0], &state_b_0[0, 0],
         &transfer_k[0, 0], &transfer_m[0, 0], &output_x[0, 0])

    return transfer_k, transfer_m, output_x

def finalise():
    finalise_()
