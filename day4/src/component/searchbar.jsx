function SearchBar({
  search,
  setSearch,
}) {
  return (
    <div className="box">
      <h2>Search Users</h2>

      <input
        type="text"
        placeholder="Search by name..."
        value={search}
        onChange={(e) =>
          setSearch(e.target.value)
        }
      />
    </div>
  );
}

export default SearchBar;