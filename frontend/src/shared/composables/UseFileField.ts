export function useFileField(form: Record<string, any>, key: string) {
  const onChange = (e: Event) => {
    const target = e.target as HTMLInputElement;
    if (!target.files?.length) return;

    form[key] = target.files[0];
  };

  return { onChange };
}
