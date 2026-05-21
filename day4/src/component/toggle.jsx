import { useState } from "react";

function Toggle() {
  const [isOn, setIsOn] = useState(false);

  return (
    <div className="box">
      <h2>Toggle Component</h2>

      <h3>
        Status :
        {isOn ? " ON" : " OFF"}
      </h3>

      <button
        onClick={() => setIsOn(!isOn)}
      >
        Toggle
      </button>
    </div>
  );
}

export default Toggle;