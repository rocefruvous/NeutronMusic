export function useFormBuilder() {
  const toFormData = (form: Record<string, any>) => {
    const data = new FormData();

    Object.entries(form).forEach(([key, value]) => {
      if (value === null || value === undefined) return;

      // handle files
      if (value instanceof File) {
        data.append(key, value);
        return;
      }

      // handle arrays
      if (Array.isArray(value)) {
        value.forEach((v, i) => {
          data.append(`${key}[${i}]`, v);
        });
        return;
      }

      data.append(key, value);
    });

    return data;
  };

  return { toFormData };
}
