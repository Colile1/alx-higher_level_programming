#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about a Python list.
 * @p: Pointer to the PyObject representing the list.
 */
void print_python_list(PyObject *p) {
    PyListObject *list;
    Py_ssize_t i, size;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; ++i) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object.
 * @p: Pointer to the PyObject representing the bytes object.
 */
void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes;
    Py_ssize_t size, i;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));

    printf("  first %d bytes: ", (int)size < 10 ? (int)size : 10);
    for (i = 0; i < (size < 10 ? size : 10); ++i) {
        printf("%02x%c", (unsigned char)PyBytes_AS_STRING(p)[i], i + 1 < (size < 10 ? size : 10) ? ' ' : '\n');
    }
}
