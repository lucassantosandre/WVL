import React from "react";

function Upload({ setFile }) {
  return (
    <div>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
    </div>
  );
}

export default Upload;
