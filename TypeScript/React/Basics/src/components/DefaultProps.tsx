
type GreetProps = {
  name?: string;
  shout?: boolean;
}
const DefaultProps = ({name = "Guest", shout = false}: GreetProps) => {
  const text: string = shout  ? name.toUpperCase() : name;

  return <p>Hi {text}</p>
}

export default DefaultProps