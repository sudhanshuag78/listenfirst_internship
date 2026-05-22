function UserCard({ user }) {
  return (
    <div className="card">
      <h2>{user.name}</h2>

      <p>
        <strong>Email:</strong> {user.email}
      </p>

      <p>
        <strong>City:</strong> {user.city}
      </p>

      <p>
        <strong>Company:</strong> {user.company}
      </p>
    </div>
  );
}

export default UserCard;