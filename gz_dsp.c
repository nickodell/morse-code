#include "Python.h"
#include "arrayobject.h"
#include "gz_dsp.c"
#include <math.h>

static PyMethodDef gz_dsp_methods {
	{"gz_dsp", gz_dsp, METH_VARARGS, "Calculate the intensity of a particular frequency. Args are (samples, freq) \
	samples is a 1d numpy array."}
	{NULL, NULL, 0, NULL}
};

float goertzel(float freq, int size, float x[])
{
	int i;
	float coeff;
	float s, s_prev1 = 0.0f, s_prev2 = 0.0f;

	coeff = 2.0f * cosf(2.0f * M_PI * freq);

	for (i = 0; i < size; i++) {
		s = x[i] + (coeff * s_prev1) - s_prev2;
		s_prev2 = s_prev1;
		s_prev1 = s;
	}

	return (s_prev1 * s_prev1) + (s_prev2 * s_prev2)
		 - (s_prev1 * s_prev2 * coeff);
}