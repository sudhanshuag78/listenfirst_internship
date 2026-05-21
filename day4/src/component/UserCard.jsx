function UserCard({ user }) {
  return (
    <div className="user-card">
      <h3>{user.name}</h3>

      <p>
        <strong>Email:</strong>
        {user.email}
      </p>

      <p>
        <strong>Phone:</strong>
        {user.phone}
      </p>

      <p>
        <strong>Website:</strong>
        {user.website}
      </p>
    </div>
  );
}

export default UserCard;