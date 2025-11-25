import { Panel } from "./components/ChildrenReactNode"
import DefaultProps from "./components/DefaultProps"
import { UserCard } from "./components/Props"


function App() {

  return (
    <div>
      <UserCard id='1' name="Priyanshu" subTitle="hello" />
      <DefaultProps name="Aashu" shout={true}/>
      <Panel title="Panel" children={
        <ul>
          <li>one</li>
        </ul>
      }/>
    </div>
  )
}

export default App
