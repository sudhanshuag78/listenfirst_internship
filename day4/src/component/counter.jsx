import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div className="box">
      <h2>Counter Component</h2>

      <h1>{count}</h1>

      <div className="button-group">
        <button
          onClick={() => setCount(count + 1)}
        >
          Increase
        </button>

        <button
          onClick={() => setCount(count - 1)}
        >
          Decrease
        </button>
      </div>
    </div>
  );
}

export default Counter;