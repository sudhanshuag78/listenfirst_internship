import { useEffect, useState } from "react";

import Counter from "./component/counter";
import Toggle from "./component/Toggle";
import SearchBar from "./component/SearchBar";
import UserList from "./component/UserList";

import "./App.css";

function App() {
  const [users, setUsers] = useState([]);

  const [search, setSearch] = useState("");

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())

      .then((data) => {
        setUsers(data);

        setLoading(false);
      })

      .catch(() => {
        setError("Failed to fetch users");

        setLoading(false);
      });
  }, []);

  const filteredUsers = users.filter((user) =>
    user.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="container">
      <h1 className="title">React Practice Project</h1>

      <Counter />

      <Toggle />

      <SearchBar
        search={search}
        setSearch={setSearch}
      />

      {loading && <h2>Loading...</h2>}

      {error && <h2>{error}</h2>}

      {!loading && !error && (
        <UserList users={filteredUsers} />
      )}
    </div>
  );
}

export default App;